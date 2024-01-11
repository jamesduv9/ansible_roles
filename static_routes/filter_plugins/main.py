from ipaddress import IPv4Network

class FilterModule():
    def filters(self):
        return {
            "mask_to_cidr": self.mask_to_cidr
        }
    
    @staticmethod
    def mask_to_cidr(mask: str):
        """
        Accepts a mask ex. 255.255.255.255
        returns a cidr prefix length ex. /32
        """
        mask = IPv4Network(f"0.0.0.0/{mask}")
        return mask.prefixlen
