# jason-voice-ai
Jason is a project for school, do not take it seriously, it is still in development.

## Parameters
You can put your own API key in `jason.py` to make it work, also, in the folder `images` you can introduce details about the faces you want to recognize and give the prompt details about the people you want Jason to recognize so he can know who they are and how to answer them.

## Running
- Save the images you want to save in the `images` folder.
- Run `face.py`, this will encode all the photos in the `images` folder and save them in a .pkl file; your computer won't have to encode all the images each time you run the assistant.
- Run `jason.py` once you saved the encodings in a pickle file so it doesn't have to encode all the images each time you run the assistant.
