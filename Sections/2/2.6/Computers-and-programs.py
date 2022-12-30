"""
The processor starts by executing the instruction at location 0.
The processor next executes the instruction at location 1, then location 2. 'Next' keeps track of the location of the next instruction.
The Jmp instruction indicates that the next instruction to be executed is at location 0, so Next is assigned with 0.
The processor executes the instruction at location 0, performing the same sequence of instructions over and over again.

Instructions represented by as 0s and 1s are known as machine instructions, and a sequence of machine instructions together form an executable program (sometimes just called an executable).
"""

"""
Steps to writing a program

1. A programmer writes a high-level program.
2. The programmer runs a compiler, which converts the high-level program into an executable program.
3. Users can then run the executable.
"""

"""
Clock: A processor's instructions execute at a rate governed by the processor's clock, which ticks at a specific frequency. Processors have clocks that tick at rates such as 1 MHz (1 million ticks/second) for an inexpensive processor ($1) like those found in a microwave oven or washing machine, to 1 GHz (1 billion ticks/second) for costlier ($10-$100) processors like those found in mobile phones and desktop computers. Executing about 1 instruction per clock tick, processors thus execute millions or billions of instructions per second.
"""

"""


A disk is able to store Terabytes of data and may contain various programs such as ProgA, ProgB, Doc1, Doc2, and OS. The memory is able to store Gigabytes of data. User runs ProgA. The disk spins and the head loads ProgA from the disk, storing the contents into memory.
The OS runs ProgB. The disk spins and the head loads ProgB from the disk, storing the contents into memory.
The OS lets ProgA run again. ProgA is already in memory so there is no need to read ProgA from the disk.

"""

"""
Why Whitespace matters



1. This program for online meetings not only does computations like scheduling and creating a unique meeting ID, but also outputs text formatted neatly for a calendar event.
2. A calendar program may append more text after the meeting invitation text.
3. The programmer of the invitation on the right wasn't careful with whitespace. "Join meeting" is buried, the link is hard to see, and the "Phone" text is dangling at a line's end.
4. The programmer also didn't end with a newline, causing subsequent text to appear at the end of a line, and even wrap to the next line. This output looks unprofessional.

"""

"""