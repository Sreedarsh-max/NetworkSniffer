from scapy.all import sniff

def packet_callback(packet):
    """Callback function to process captured packets."""
    print(packet.summary())

def main():
    print("Starting network sniffer... Press Ctrl+C to stop.")
    # Capture packets (sniff) and apply the callback function to each packet
    try:
        sniff(prn=packet_callback, store=False)
    except KeyboardInterrupt:
        print("\nSniffer stopped.")

if __name__ == "__main__":
    main()
