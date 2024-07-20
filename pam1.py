import numpy as np
import matplotlib.pyplot as plt

def manchester_encode(data):
    """
    Manchester encode a sequence of binary data.
    """
    encoded_data = []
    for bit in data:
        if bit == 0:
            encoded_data.extend([1, -1])  # High-to-low transition for 1
        else:
            encoded_data.extend([-1, 1])  # Low-to-high transition for 0
    return encoded_data

def calculate_psd(signal, sampling_rate):
    """
    Calculate the Power Spectral Density (PSD) of a signal.
    """
    n = len(signal)
    fft_result = np.fft.fft(signal)
    psd = np.abs(fft_result) ** 2 / n
    freqs = np.fft.fftfreq(n, 1 / sampling_rate)
    return freqs, psd

# Example usage
data = [1, 0, 1, 1, 0, 0, 1, 0]  # Example binary data
sampling_rate = 1000  # Sample rate in Hz

# Manchester encode the data
encoded_signal = manchester_encode(data)

# Calculate PSD
freqs, psd = calculate_psd(encoded_signal, sampling_rate)

# Plot input binary data
plt.figure(figsize=(10, 6))
plt.subplot(2, 1, 1)
plt.stem(range(len(data)), data, use_line_collection=True)
plt.title('Input Binary Data')
plt.xlabel('Time')
plt.ylabel('Value')
plt.grid(True)

# Plot PSD
plt.subplot(2, 1, 2)
plt.plot(freqs[:len(freqs)//2], psd[:len(psd)//2])  # Plot only positive frequencies
plt.title('Power Spectral Density (PSD) of Manchester Encoded PAM Signal')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Power')
plt.grid(True)

plt.tight_layout()
plt.show()
