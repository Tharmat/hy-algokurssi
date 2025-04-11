import mido

# TODO: Checks only the latest tempo change. If file contains multiple tempo changes, will affect timing
def get_tempo(mid):
    for msg in mid:
        if msg.type == 'set_tempo':
            tempo = msg.tempo
            print("Tempo is:", tempo)
    return tempo

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

def play_midi(midi_file):
    for msg in midi_file.play():

        # For debugging: print the event being played
        print(msg)
        port.send(msg)

# TODO: WIP, requires more though and cleaning up. This is just a prototype for processing the midi events and eventually will save everything into a trie data
# structure for applying Markov chains
def process_midi(new, old):
    # Loop through existing midi track, pick only note_on and note_off events (or note_on with velocity = 0) and create a new track with fixed duration of notes
    for x, msg in enumerate(old):

        # Filter out meta messages
        if not msg.is_meta:
            if msg.type == 'note_on' and msg.velocity != 0:

                # TODO: Quantize note lenghts if tempo information is wanted
                note_duration = 0

                for i in range(x + 1, len(old)):
                    next_message = old[i]
                    note_duration += next_message.time

                    if next_message.type == 'note_on' and next_message.velocity == 0:
                        break
                
                # For debugging. Note duration works in a weird magical way in midi files and does not not correspond to more traditional BPM
                # print("Note duration is:", mido.tick2second(note_duration, mid.ticks_per_beat, tempo))

                # TODO: Create an approach where the note duration is quantized, but the note order is saved. I.e. for every read note_on, calculate the note 
                # duration, put the note_on in <data_structure> and when processing reaches the appropriate note_off remove from the data structure. 
                # Current implementation is strictly first-come-first-serve basis and forces the stream to be monophonic 
                new.append(mido.Message('note_on', channel = msg.channel, note = msg.note, velocity = msg.velocity, time = 1))
                new.append(mido.Message('note_on', channel = msg.channel, note = msg.note, velocity = 0, time = mido.second2tick(0.5, mid.ticks_per_beat, tempo)))


# Debug - list available midi interfaces
print(mido.get_output_names())

# Use the first found midi interface for output
port = mido.open_output(mido.get_output_names()[0])

# Ingest a hard coded midi file - The classic Doom E1M1
mid = mido.MidiFile('../data/midi/doom1/e1m7.mid')

# List what and how many midi notes each track contains for checking which tracks are "melodic"
list_track_details(mid.tracks)

# Set tempo
tempo = get_tempo(mid)

# Create new temp midi file for populating with processed midi events for eventual playback
new_file = mido.MidiFile()
new_file.ticks_per_beat = mid.ticks_per_beat

# Midi file must contains at least one track to be playable
new_track = mido.MidiTrack()

# Hard code the track for debugging
TRACK = 1

# Process the given midi file to onclude only note_on and note_off events and quantize everything to fixed amount
process_midi(new_track, mid.tracks[TRACK])

new_file.tracks.append(new_track)
new_track.append(mido.MetaMessage('set_tempo', tempo=tempo))

# Play the newly constructed midi file
play_midi(new_file)