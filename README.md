# cses-standings
Receives a list of CSES users and outputs a static site with standings.

## Usage
`python3 main.py --help`

## Users file
One user per line, following the format `id:name`. The id must match the CSES profile id, and the name
can be anything.
Example `users.txt`:
```
1231:Alice
4142:Bob
3543:OtherName
```

## TODO
This is work in progress. Some pending stuff:
* Improve documentation
* Add images to README
* Clear up the code
* Add github actions example
