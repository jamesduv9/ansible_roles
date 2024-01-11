# static_routes
Configure static routes for IOS-XE and NXOS in an IaC fashion. Assumes a standard way of defining static routes in your host vars.

Ex.
```
host_static_routes:
  - nh: 10.2.2.2
    destination: 100.2.2.2
    mask: 255.255.255.255
    metric: 10
  - nh: 123.123.123.123
    mask: 255.0.0.0
    destination: 192.0.0.0
    metric: 20
```
##Workflow
1. Get current config
2. Get desired config (templated host vars)
3. Find lines in current config that aren't in desired config, append "no "
4. Append desired config to end of list
5. Send to device


##Custom Filter
Uses a single custom filter `mask_to_cidr` to accept a subnet in format 255.255.255.255 and return it in prefix length format (ex. 32). This is needed for converting to nxos configs