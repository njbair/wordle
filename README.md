# YAWS: Yet Another Wordle Solver

A simple Wordle solver with declarative configuration.

## First-Time Initialization

Before using the script, you'll need to download the word list. Use the _fetchwords.py_ script:

```
fetchwords.py
```

This will download a huge word list from [dwyl/englishwords](https://github.com/dwyl/english-words), then filter it down to only 5-letter words, and save it to _five-letter-words.json_.

## Configuration

Edit or create the file _config.yaml_. You can start by copying the included _config.example.yaml_:

```
cp config.example.yaml config.yaml
vi config.yaml
```

Make your first Wordle guess. Let's say it looks like this:

![POLAR](assets/example.png)

You can represent this result in the config file as follows:

```
spaces:
- []
- exclude: O
- L
- exclude: A
- []
include: OLA
exclude: PR
```

Syntax for the **spaces** property:
- Represent an unknown space with an empty list (**[]**)
- If you know a space should not include certain letters, use the **exclude** property to list them (**exclude: ABC**).
- If you know the letter, just use a string (**L**).

Note: to define multiple letters for include/exclude properties, you can use list syntax instead of a string, if you prefer (**exclude: [A,B,C]**)

The **include** property specifies letters that must be present in a valid result. This should be a list of all green and yellow letters in your puzzle.

The **exclude** property specifies letters that must not be present in a valid result. This should be a list of all gray letters in your puzzle.

## Usage

Once you've configured the script, run it like so:

```
python yaws.py
```

This will spit out a list of potential words. Choose the best one from this list and try it in your puzzle. If it works, you're done. If not, update the config with any new clues and try again.

That's it!