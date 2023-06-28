import pygame
import sys
import simpleaudio as sa
import numpy as np

def make_sound(hz):
    frequency = hz  # Our played note will be 440 Hz
    fs = 44100  # 44100 samples per second
    seconds = 5  # Note duration of 3 seconds

    # Generate array with seconds*sample_rate steps, ranging between 0 and seconds
    t = np.linspace(0, seconds, seconds * fs, False)

    # Generate a 440 Hz sine wave
    note = np.sin(frequency * t * 2 * np.pi)

    # Ensure that highest value is in 16-bit range
    audio = note * (2**15 - 1) / np.max(np.abs(note))
    # Convert to 16-bit data
    audio = audio.astype(np.int16)

    # Start playback
    try:
        sa.play_buffer(audio, 1, 2, fs)
    except:
        print('error')


def main():
    pygame.init()

    # Set the caption of the screen
    pygame.display.set_caption('Synth')

    screen = pygame.display.set_mode((500, 500))
    clock = pygame.time.Clock()

    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    make_sound(220)
                if event.key == pygame.K_d:
                    make_sound(246)
                if event.key == pygame.K_s:
                    make_sound(261)  
                if event.key == pygame.K_w:
                    make_sound(293)    
                if event.key == pygame.K_q:
                    make_sound(329) 
                if event.key == pygame.K_e:
                    make_sound(349) 
                if event.key == pygame.K_r:
                    make_sound(392) 
                if event.key == pygame.K_f:
                    make_sound(440)             
        screen.fill((234, 212, 252))

        pygame.display.update()
        clock.tick(60)

if __name__ == "__main__":
    main()