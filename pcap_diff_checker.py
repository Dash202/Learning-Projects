import pyshark
pcap1 = pyshark.FileCapture('Test_Capture.pcapng')
pcap2 = pyshark.FileCapture('Test_Capture2.pcapng')


pcap1_ids = list()
pcap2_ids = list()

for pkt1 in pcap1:
	try:
		ip_id1 = pkt1['ip'].id
		pcap1_ids.append(ip_id1)
	except:
		continue
#print(ip_id)
for pkt2 in pcap2:
	try:
		ip_id2 = pkt2['ip'].id
		pcap2_ids.append(ip_id2)
	except:
		continue

#print("Capture 1 IDs: ", pcap1_ids)
#print("Capture 2 IDs: ", pcap2_ids)

for id1 in pcap1_ids:
	
		print("Missing Packet ID:", id1)
		#print(pcap2_ids)
	elif id1 is pcap2_ids:
		print(id1, "is present in both captures")
#print(pcap2_ids)
print("Finished")


'''
for id1 in pcap1_ids:
	if id1 is not pcap2_ids:
		print("Missing Packet ID:", id1)
		#print(pcap2_ids)
	elif id1 is pcap2_ids:
		print(id1, "is present in both captures")
#print(pcap2_ids)
print("Finished")
'''














