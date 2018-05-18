# Coind
A bitcoind based wallet manager in Python

## Getting Started
This is a cryptocurrency wallets management using Python, compatible with all bitcoind forked daemon.
It will turn possible to execute commands like "-daemon" to "walletpassphrase"

### Simple example
```
from coind import Coind

coind = Coind('vsync', Coind.TYPE_CLI)
raw_result = coind.run('getinfo')
print(raw_result)
```

### Description
Coind class has some parameters to define daemon execution:
- (Required) **name**: coin name
- (Required) **type**: coin daemon type. Currently exists:
  - type d (```Coind.TYPE_D```): like digitalpriced, all commands will be executed directly in daemon
  - type cli (```Coind.TYPE_CLI```): like vsync-cli, wallet management is executed separately from daemon
- (Optional) **path**: if daemon could not be execute from any directory, need to set the directory where the daemon is
- (Optional) **debug**: will print some logs to debug class execution

### Prerequisites
- Python 3

### Installing
```
pip install coind
```

### Running the tests
```
./tests/run.py
```

### Additional warning
After using -daemon commands, it's recommended to wait some minutes for application turn ready

### License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details

### Donation
#### Bitcoin
﻿1Hp2hrMU3FUdCtTR9AdwEK7zhKarSENmRY

#### Dash
XcN1iszFQFKKwwrAM69uvx8BPu8cY3cWCf

#### Solaris XLR
SZMw57FKCxcSM8XKqqq8iL89J8xxgunLNq

#### Vsync VSX
﻿VDeD4nt5gDRfageB4K3HwGCJHNDyyu8U3R