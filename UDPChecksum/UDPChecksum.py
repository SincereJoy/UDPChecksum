import matplotlib.pyplot as plt
from matplotlib.widgets import TextBox, Button

textbox1 = TextBox(plt.axes([0.3, 0.8, 0.5, 0.080]), '1st 16-bit number: ')
textbox2 = TextBox(plt.axes([0.3, 0.7, 0.5, 0.080]), '2nd 16-bit number: ')
textbox3 = TextBox(plt.axes([0.3, 0.6, 0.5, 0.080]), '3rd 16-bit number: ')
calButton = Button(plt.axes([0.4, 0.4, 0.3, 0.080]), 'Calculate')

# Calculate the checksum
# source is the datagram string, count is the amount of 16-bit numbers contained in the string
def calChecksum(source, count):
    sum = 0
    # Split the source string
    for i in range(count):
        sum += int(source[i*16:(i+1)*16], 2)
    # Handle the carry bit
    if sum >= (0b1 << 16):
        sum = sum + 0b1
        sum -= (0b1 << 16)
    result = '{:016b}'.format((0b1 << 16) - 1 - sum)
    return result

# calButton click event
def onButtonClick(event):
    # Format the inuput numbers to 16-bit
    text1 = '{:016b}'.format(int(textbox1.text, 2))
    text2 = '{:016b}'.format(int(textbox2.text, 2))
    text3 = '{:016b}'.format(int(textbox3.text, 2))
    # Calculate and show the checksum
    sourceString = text1+text2+text3
    resultBox = TextBox(
        plt.axes([0.3, 0.1, 0.5, 0.080]), 'Checksum: ', calChecksum(sourceString, 3))
    plt.draw()


calButton.on_clicked(onButtonClick)
plt.show()
