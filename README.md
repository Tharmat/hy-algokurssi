# HY-algokurssi
Repository for University of Helsinki Algorithmic Project course

## Description of the project
This project is done for University of Helsinki's course "Aineopintojen harjoitustyö: Algoritmit ja tekoäly" (Project: Algorithms and AI). It's main purpose is to implement a Markov-chain based music generation system using trie data structure. 

## Architecture of the project
The architecture can be roughly divided into three section:
1. Data crunching: ingesting MIDI files, cleaning up the data by doing appropriate transformations, calculating the probabilities for the Markov chains and then exporting/serializing the results to a JSON file
2. The actual generation algorithmic part for generating music using Markov chains: ingesting precalculated probabilities from a JSON file and generating new melodies based on parameters
3. Light-weight web-based GUI for previous as well as in-browser MIDI-playback for the results

## The data 
The plan is to use freely-available General MIDI (GM) compliant MIDI-files for data. This is because GM compliant files have a fixed allocation of instruments which helps to narrow down the data to melodic parts only. 

## Use of AI in this project
As per course guidelines, the use of AI has to be documented for this project. As of now, AI has been used as a "sparring partner" for coming up with the general idea for the implementation as well as for generic help related to Python syntax and or/syntax (as it is not my "first language") 
