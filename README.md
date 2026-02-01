# Crash Handler
![A sad Charlie holding a sign with an X inside a red circle.](/assets/images/error.png)

A basic crash handler you can put anywhere, so long as you implement closing right!

## How does it work?
It hosts a TCP Server at `localhost:6961` that listens to anything.

If anything requests anything to this TCP Server, it'll assume the application it's monitoring is closing normally, so, it'll kill itself.

If the application closes without sending anything, the crash window will appear!

## What parameters can I put in it?
| Parameter             | Description (* = REQUIRED) |
|-----------------------|----------------------------|
|`--monitor-pid=INTEGER`|The process ID to monitor*  |

## Examples
They can be found in this Repository's Website!
