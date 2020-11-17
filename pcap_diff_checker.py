import pyshark
pcap = pyshark.FileCapture('Test_Capture.pcapng')

for pkt in pcap:
	try:
		print(pkt['ip'].src)
	except:
		continue


#print(pcap)
















