from collections import deque

# Rolling buffers for both markers
sop_buffer = deque(maxlen=4)
som_buffer = deque(maxlen=14)

with open('input.txt', 'r') as f:
    index = 0
    found_sop = False
    while ch := f.read(1):
        sop_buffer.append(ch)
        som_buffer.append(ch)
        index += 1

        # Detect the start of packet marker
        if not found_sop and index >= 4 and len(set(sop_buffer)) == 4:
            print(f'(1) Start of packet: {index}')
            found_sop = True

        # Detect the start of message marker
        if index >= 14 and len(set(som_buffer)) == 14:
            print(f'(2) Start of message: {index}')
            break
