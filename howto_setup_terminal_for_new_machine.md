> WIP

# Setup a zsh terminal in a new machine

> WARNING: this HOWTO has some personal preferences on how to setup a `zsh` terminal in a Linux machine.
> Most choices can be modified, removed or added at will. Here I will present a base from which to setup the terminal

The idea is to have a `.sh` to setup the following:
- zsh
with some additional options.

Programs to add:
- zoxide
- zfz
- micromamba (uv in the future?)

You can find the setup file in this github repo [dotfiles]

## zsh

### Options
The following options can be set in the `.zshrc` file when following the `setopt` option
- `correct`: Try to correct the spelling of commands
- `extendedglob`: Extended globbing. Allows using regular expressions with *
- `nocaseglob`: case insensitive search
- `appendhistory`: append history in `.zsh_hystory` instead opf overwrite it
- `histignorespace`: don't save commands that start with space

```bash
zstyle ':completion:*' matcher-list 'm:{[:lower:][:upper:]}={[:upper:][:lower:]}' # Case insensitive tab completion
zstyle ':completion:*' list-colors "${(s.:.)LS_COLORS}"         # Colored completion (different colors for dirs/files/etc)
# Speed up completions
zstyle ':completion:*' accept-exact '*(N)'
zstyle ':completion:*' use-cache on
zstyle ':completion:*' cache-path ~/.zsh/cache
```

### Alias
```bash
alias cp="cp -i"                                                # Confirm before overwriting something
alias df='df -h'                                                # Human-readable sizes
alias l='ls -Flrth'
```

## Programs

## References
- This [github repo](https://github.com/bartekspitza/dotfiles/tree/master) related to [this beautiful video](https://youtu.be/mSXOYhfDFYo?si=eoGr-QExQI17AKhR0)
- The [manjaro zsh personalization](https://github.com/Chrysostomus/manjaro-zsh-config) which inspired a lot of option for zsh
