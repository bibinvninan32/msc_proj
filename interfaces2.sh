sudo ip link add veth-r-cont type veth peer name veth-r-ovs
sudo ip link add veth-r-inter type veth peer name veth-b-inter
sudo ip link add veth-b-cont type veth peer name veth-b-ovs

