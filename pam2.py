import numpy as np
import matplotlib.pyplot as plt

def manchester_encode(data, pulse_duration):
    """
    Manchester encode a sequence of binary data using rectangular pulses.
    """
    encoded_data = []
    for bit in data:
        if bit == 0:
            encoded_data.extend([-1] * pulse_duration)  # Low level for duration
            encoded_data.extend([1] * pulse_duration)   # High level for duration
        else:
            encoded_data.extend([1] * pulse_duration)   # High level for duration
            encoded_data.extend([-1] * pulse_duration)  # Low level for duration
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
pulse_duration = 10  # Duration of each pulse in samples

# Manchester encode the data with rectangular pulses
encoded_signal = manchester_encode(data, pulse_duration)

# Calculate PSD
freqs, psd = calculate_psd(encoded_signal, sampling_rate)

# Plot input binary data

plt.figure(figsize=(10, 6))
plt.title('Ansh Srivastava -102106016')
plt.subplot(3, 1, 1)
plt.stem(range(len(data)), data, use_line_collection=True)
plt.title('Input Binary Data')
plt.xlabel('Time')
plt.ylabel('Value')
plt.grid(True)

# Plot Manchester encoded signal
plt.subplot(3, 1, 2)
plt.plot(encoded_signal)
plt.title('Manchester Encoded Signal')
plt.xlabel('Time (x 100)')
plt.ylabel('Amplitude')
plt.grid(True)

# Plot PSD
plt.subplot(3, 1, 3)
plt.plot(freqs[:len(freqs)//2], psd[:len(psd)//2])  # Plot only positive frequencies
plt.title('Power Spectral Density (PSD) of Manchester Encoded PAM Signal')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Power')
plt.grid(True)
plt.suptitle('Ansh Srivastava - 102106016 ')
plt.tight_layout()
plt.show()
