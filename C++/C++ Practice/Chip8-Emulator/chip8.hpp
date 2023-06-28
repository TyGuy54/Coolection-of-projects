#pragma once // enusures that this header file will not be included multiple times
#include <cstdint>
#include <chrono>
#include <random>
using namespace std;

// quick notes: 
//  - uint8_t is shorthand for a type of unisigned intiger thats 8 bits long
//  - uint16_t is shorthand for a type of unisigned intiger thats 16 bits long

// unisigned ints are intigers that cant be negitive
const unsigned int REGISTER_COUNT = 16;
const unsigned int MEMORY_SIZE = 4096;
const unsigned int STACK_LEVELS = 16;
const unsigned int VIDEO_HEIGHT = 32;
const unsigned int VIDEO_WIDTH = 64;
const unsigned int KEY_COUNT = 16;


class Chip8{
    // The Chip8 has 16 8-bit instructions
    public:
        Chip8(); // constructer declaration
        void loadRom(const char* filename); // method declaration
        void Cycle();

        uint8_t keypad[KEY_COUNT];
        uint32_t video[VIDEO_HEIGHT * VIDEO_WIDTH];

    private:
        // Chip 8 instructions
        void Table0();
        void Table8();
        void TableE();
        void TableF();

        // Do nothing
        void OP_NULL();

        // clears screen
        void OP_00E0();

        // returns from a subroutine
        void OP_00EE();

        // jump to location nnn
        void OP_1nnn();

        // call subroutine at location nnn
        void OP_2nnn();

        // Skips the next instruction if Vx == kk
        void OP_3xkk();

        // skips the next instruction if Vx != kk
        void OP_4xkk();

        // skip next instruction if Vx == Vy
        void OP_5xy0();

        // set Vx = kk
        void OP_6xkk();

        // set Vx = vx + kk
        void OP_7xkk();

        // set Vx == Vy
        void OP_8xy0();

        // set Vx = Vx OR Vy
        void OP_8xy1();

        // set Vx = Vx AND Vy
        void OP_8xy2();

        // set Vx = Vx XOR Vy
        void OP_8xy3();

        // sett Vx = Vx + Vy, set VF = carry
        void OP_8xy4();

        // set Vx = Vx - Vy, set VF = NOT borrow
        void OP_8xy5();

        // set Vx = Vx SHR 1
        void OP_8xy6();

        // set Vx = Vy - Vx, set VF = NOT borrow
        void OP_8xy7();

        // set Vx = Vx SHL 1
        void OP_8xyE();

        // skip next instruction if Vx != Vy
        void OP_9xy0();

        // set I == nnn
        void OP_Annn();

        // jump to location nnn + V0
        void OP_Bnnn();

        // set Vx = random byte AND kk
        void OP_Cxkk();

        // display n-byte sprite starting at memory location I at (Vx, Vy), set VF = collision
        void OP_Dxyn();

        // skip next instruction if key with value of Vx is pressed
        void OP_Ex9E();

        // skip next if key with value Vx is not pressed
        void OP_ExA1();

        // set Vx == delay timer value
        void OP_Fx07();

        // wait for a key press, store the value of the key in Vx
        void OP_Fx0A();

        // set delay timer = Vx.
        void OP_Fx15();

        // set sound timer = Vx.
        void OP_Fx18();

        // set I = I + Vx.
        void OP_Fx1E();

        // set I = location of sprite for digit Vx
        void OP_Fx29();

        // store BCD representation of Vx in memory locations I, I+1, and I+2
        void OP_Fx33();

        // store registers V0 through Vx in memory starting at location I.
        void OP_Fx55();

        // read registers V0 through Vx from memory starting at location I
        void OP_Fx65();


        uint8_t registers[REGISTER_COUNT]; // a register is a dedicated location on a CPU for storage
        uint8_t memory[MEMORY_SIZE]; // the Chip8 has 4096 bytes of memory
        uint16_t index; // index register
        uint8_t pc; // program counter
        uint16_t stack[STACK_LEVELS];
        uint8_t sp; // stack pointer
        uint8_t delayTimer;
        uint8_t soundTimer;
        uint16_t opcode; // an opcode specifies the operation to be pregormed

        // used to get a random number
        default_random_engine randGen;
        uniform_int_distribution<uint8_t> randByte;

        typedef void (Chip8::*Chip8Func)();
        Chip8Func table[0xF + 1]{&Chip8::OP_NULL};
        Chip8Func table0[0xE + 1]{&Chip8::OP_NULL};
        Chip8Func table8[0xE + 1]{&Chip8::OP_NULL};
        Chip8Func tableE[0xE + 1]{&Chip8::OP_NULL};
        Chip8Func tableF[0x65 + 1]{&Chip8::OP_NULL};

};