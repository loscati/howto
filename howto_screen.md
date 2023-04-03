# How to GNU `screen`: a very brief guide

#### Create a session
```bash
screen -S session_name
```

#### Detach current screen
```bash
ctrl+a d
```
Note: you have to keep `ctrl` pressed while pressing `a` and then `d`.

#### Reattach to a session
```bash
screen -R session_name
```

#### Close a session
```bash
ctrl+a \
```
Note: `\` has to be pressed without pressing the `crtl` key. This is safer than writing directly inside the session:
```bash
exit
```
because it will ask you if you are sure to close the session, on the other hand `exit` will brutally exit the session. **Be careful**, once the session is closed it cannot be restored.

#### List of current sessions
```bash
screen -ls
```
