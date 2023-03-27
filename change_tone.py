import librosa
import soundfile as sf
import os

from lib.args import args
from lib.write import create_dirs

from tqdm import tqdm


if args.unique:
    if args.gender == 'female':
        shifts = [args.shift]
        
    elif args.gender == 'male':
        shifts = [-args.shift]
        
    else:
        shifts = [-args.shift, args.shift]

else:
    start = args.minimum if args.gender == 'female' else -args.shift
    end = -args.minimum + 1 if args.gender == 'male' else args.shift + 1
    shifts = range(int(start), int(end))

if args.input:
    files = [args.input]
    
else:
    files = os.listdir(args.directory)
    
if os.path.isfile(args.output) or os.path.islink(args.output):
    print ('output can\'t be a file or a link')
    exit()
    
create_dirs(args.output)

for file in tqdm(files, desc='files', position=1):
    
    if args.directory:
        filepath = os.path.join(args.directory, file)
        
    else :
        filepath = file
        
    # Create path and filename
    split_name = os.path.basename(filepath).split('.')
    extension = split_name[-1]
    name = split_name[0]
        
    # check input and output
    if not os.path.isfile(filepath) or extension not in ['mp3', 'wav']:
        print (f'{file} is not a valid music file')
        continue
        
    # Load the audio file
    audio, sr = librosa.load(filepath, sr=None)
        
    for shift in tqdm(shifts, desc='pitch shifting', position=2):
        
        # Evade original tone
        if not args.force and shift in range(-1, 2):
            continue
            
        # Perform pitch shifting
        audio_shifted = librosa.effects.pitch_shift(audio, sr=sr, n_steps=shift)
        
        tone = 'low' if shift < 0 else 'high'
        filename = '_'.join([name, tone, str(abs(shift))]) + '.' + extension
        path = os.path.join(args.output, filename)
        
        # Save the shifted audio to a file
        sf.write(path, audio_shifted, sr)