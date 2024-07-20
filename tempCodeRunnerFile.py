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