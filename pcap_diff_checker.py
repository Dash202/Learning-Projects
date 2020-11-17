import pyshark
pcap = pyshark.FileCapture('Test_Capture.pcapng')

for pkt in pcap:
	try:
		src = pkt['ip'].src
		dst = pkt['ip'].dst
		ip_id = pkt['ip'].id
		udp_port = pkt['udp'].srcport
		#print("Source:", src, "Destination:", dst)
		#print(ip_id)
		print(udp_port)
	except:
		continue

#print(pcap)
















