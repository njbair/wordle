# YAWS: Yet Another Wordle Solver

A simple Wordle solver with declarative configuration.

## First-Time Initialization

Before using the script, you'll need to download the word list. Use the _fetchwords.py_ script:

```
fetchwords.py
```

This will download a huge word list from [dwyl/englishwords](https://github.com/dwyl/english-words), then filter it down to only 5-letter words, and save it to _five-letter-words.json_.

## Configuration

Edit or create the file _config.json_. You can start by copying the included _config.example.json_:

```
cp config.example.json config.json
vi config.json
```

Make your first Wordle guess. Let's say it looks like this:

![POLAR](assets/example.png)

You can represent this result in the config file as follows:

```
{
  "spaces": [
    {},
    { "exclude": "O" },
    "L",
    { "exclude": "A" },
    {}
  ],
  "include_letters": "OLA",
  "exclude_letters": "PR"
}
```

Syntax for the **spaces** property:
- Represent an unknown space with an empty object (**{}**)
- If you know a space should not include certain letters, use the **exclude** property to list them (**"exclude": "ABC"**).
- If you know the letter, just use a string (**"L"**).

The **include_letters** property specifies letters that must be present in a valid result. This should be a list of all green and yellow letters in your puzzle.

The **exclude_letters** property specifies letters that must not be present in a valid result. This should be a list of all gray letters in your puzzle.

## Usage

Once you've configured the script, run it like so:

```
python yaws.py
```

This will spit out a list of potential words. Choose the best one from this list and try it in your puzzle. If it works, you're done. If not, update the config with any new clues and try again.

That's it!