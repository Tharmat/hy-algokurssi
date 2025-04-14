from queue import Queue
import mido
import glob
from trie import Trie
from markov import Markov

# TODO: Checks only the latest tempo change. If file contains multiple tempo changes, will affect timing
def get_tempo(mid):
    for msg in mid:
        if msg.type == 'set_tempo':
            tempo = msg.tempo
            print("Tempo is:", tempo)
            print("---------")

    return tempo

# Returns the program change (instrument change) from the midi 
def get_instrument(track):
    for msg in track:
        if msg.type  == 'program_change':
            print("Instrument is:", msg)
            return msg
        
# List track details for debugging
def list_track_details(tracks):
    for i, track in enumerate(tracks):
        print('Track {}: {}'.format(i, track.name))
        note_information = {}

        for msg in track:
            if msg.type == 'note_on' and msg.velocity != 0:
                if msg.note not in note_information:
                    note_information[msg.note] = 0
                note_information[msg.note] += 1
        print(note_information)
    print("---------")

# Plays the given midi file
def play_midi(midi_file):
    for msg in midi_file.play():

        # For debugging: print the event being played
        print(msg)
        port.send(msg)

# TODO: WIP, requires more though and cleaning up. This is just a prototype for processing the midi events and eventually will save everything into a trie data
# structure for later use by Markov chain
def process_midi(trie, track):

    # TODO: This should be dependant on the chosen order of the Markov chain
    sliding_note_window = Queue(maxsize = 3)

    # Loop through existing midi track, pick only note_on and note_off events (or note_on with velocity = 0) and create a new track with fixed duration of notes
    for x, msg in enumerate(track):

        # Filter out meta messages
        if not msg.is_meta:
            if msg.type == 'note_on' and msg.velocity != 0:
                
                if sliding_note_window.full():
                    notes = [None] * 3
                    for x in range(3):
                        notes[x] = sliding_note_window.get()
                    
                    # Sanity check
                    assert(sliding_note_window.empty() is True)

                    sliding_note_window.put(notes[1])
                    sliding_note_window.put(notes[2])

                    trie.insertNode(notes)
                sliding_note_window.put(msg.note)
                
                # TODO: Quantize note lenghts if tempo information is wanted
                # note_duration = 0

                # for i in range(x + 1, len(old)):
                #    next_message = old[i]
                #    note_duration += next_message.time

                #    if next_message.type == 'note_on' and next_message.velocity == 0:
                #        break
                
                # For debugging. Note duration works in a weird magical way in midi files and does not not correspond to more traditional BPM
                # print("Note duration is:", mido.tick2second(note_duration, mid.ticks_per_beat, tempo))

                # TODO: Implement an option to force the notes into a specified scale
                # TODO: Create an approach where the note duration is quantized, but the note order is saved. I.e. for every read note_on, calculate the note 
                # duration, put the note_on in <data_structure> and when processing reaches the appropriate note_off remove from the data structure. 
                # Current implementation is strictly first-come-first-serve basis and forces the stream to be monophonic 
                # new.append(mido.Message('note_on', channel = msg.channel, note = msg.note, velocity = msg.velocity, time = 1))
                # new.append(mido.Message('note_on', channel = msg.channel, note = msg.note, velocity = 0, time = mido.second2tick(0.5, mid.ticks_per_beat, tempo)))    

# Debug - list available midi interfaces
print(mido.get_output_names())

# Use the first found midi interface for output
port = mido.open_output(mido.get_output_names()[0])

# List of midi files and their tracks to process, currently hard coded midi and using Doom1 and Doom2 soundtracks for testing
files = [
    {"name": "../data/midi/doom1/e1m1.mid", "track": 1},
    {"name": "../data/midi/doom1/e1m4.mid", "track": 1},
    {"name": "../data/midi/doom1/e1m9.mid", "track": 1},
    {"name": "../data/midi/doom1/e2m3.mid", "track": 1},
    ]

# List what and how many midi notes each track contains for checking which tracks are "melodic"
# list_track_details(mid.tracks)

# Basic properties for the midi file
TEMPO = 500000
TICKS = 96
INSTRUMENT = 30

# Create new temp midi file for populating with processed midi events for eventual playback
new_file = mido.MidiFile()
new_file.ticks_per_beat = TICKS

# Midi file must contains at least one track to be playable, let's call this track #0
new_track = mido.MidiTrack()
new_track.append(mido.MetaMessage('set_tempo', tempo=TEMPO))
new_track.append(mido.Message('program_change', channel = 0, program=INSTRUMENT))

new_file.tracks.append(new_track)

trie = Trie()

# Process the given midi files to include only note_on and note_off events and quantize everything to fixed amount
for file in files:
    print("Processing:", file, "track:", file["track"])
    process_midi(trie, mido.MidiFile(file["name"]).tracks[file["track"]])

# Generate series of notes based on the probabilities from the ingested midi files
markov = Markov()

# How many new tracks to generate, single track is monophonic, 3 generates triads
TRACKS = 1

# Length of notes
LENGHT = 0.25

# How much to offset different tracks
OFFSET = 0.125

print(f'Creating new midi file with {TRACKS} tracks')

for i in range(TRACKS):
    track = mido.MidiTrack()

    # How many notes to generate
    NOTES = 32
    notes = markov.run(trie, iterations = NOTES)

    track.append(mido.Message('note_off', channel = i + 1, note = 0, time = mido.second2tick(OFFSET, TICKS, TEMPO)))  

    # Create a new midi track based on the Markov-chain generated notes using fixed velocities and timing
    for note in notes:
        track.append(mido.Message('note_on', channel = i + 1, note = note, velocity = 96, time = i * OFFSET))
        track.append(mido.Message('note_off', channel = i + 1, note = note, time = mido.second2tick(LENGHT, TICKS, TEMPO)))  

    # Append a dummy sixteenth note to the end of the midi file to prevent suddent cut of playback
    track.append(mido.Message('note_off', channel = i + 1, note = 0, time = mido.second2tick(0.25, TICKS, TEMPO)))  

    new_file.tracks.append(track)

# Play the newly constructed midi file
play_midi(new_file)