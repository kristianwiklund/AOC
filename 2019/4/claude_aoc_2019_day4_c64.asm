; Advent of Code 2019 Day 4 - Commodore 64 Assembly (6502)
; Find valid passwords in range 248345-746315
; Assemble with: ca65 or ACME or DASM
; Load address: $0801 (BASIC start)

        * = $0801               ; BASIC program start

; BASIC stub: 10 SYS 2064
        .byte $0b, $08          ; Next line pointer
        .byte $0a, $00          ; Line 10
        .byte $9e               ; SYS token
        .byte $20, $32, $30, $36, $34  ; " 2064"
        .byte $00               ; End of line
        .byte $00, $00          ; End of BASIC

; Constants
SCREEN  = $0400                 ; Screen memory
COLOR   = $D800                 ; Color memory
CHROUT  = $FFD2                 ; KERNAL char output

; Zero page variables
current_lo      = $FB           ; Current password (24-bit)
current_mid     = $FC
current_hi      = $FD
end_lo          = $F8           ; End value
end_mid         = $F9
end_hi          = $FA
part1_lo        = $02           ; Part 1 counter (16-bit)
part1_hi        = $03
part2_lo        = $04           ; Part 2 counter (16-bit)
part2_hi        = $05
digits          = $10           ; Buffer for 6 digits ($10-$15)
temp1           = $20
temp2           = $21
temp3           = $22

        * = $0810               ; Start of program

start:
        ; Clear screen
        jsr clear_screen
        
        ; Print title
        ldx #0
@title_loop:
        lda title_text,x
        beq @title_done
        jsr CHROUT
        inx
        bne @title_loop
@title_done:

        ; Initialize counters
        lda #0
        sta part1_lo
        sta part1_hi
        sta part2_lo
        sta part2_hi
        
        ; Set start value: 248345 = $03CA19
        lda #$19
        sta current_lo
        lda #$CA
        sta current_mid
        lda #$03
        sta current_hi
        
        ; Set end value: 746315 = $0B6348 + 1
        lda #$49
        sta end_lo
        lda #$63
        sta end_mid
        lda #$0B
        sta end_hi

; Main loop - iterate through range
main_loop:
        ; Check if current > end
        lda current_hi
        cmp end_hi
        bcc @continue           ; current_hi < end_hi
        bne @done               ; current_hi > end_hi
        
        lda current_mid
        cmp end_mid
        bcc @continue
        bne @done
        
        lda current_lo
        cmp end_lo
        bcs @done               ; current >= end

@continue:
        ; Extract digits from current value
        jsr extract_digits
        
        ; Check Part 1
        jsr check_part1
        beq @skip_p1
        
        ; Increment Part 1 counter
        inc part1_lo
        bne @skip_p1
        inc part1_hi
        
@skip_p1:
        ; Check Part 2
        jsr check_part2
        beq @skip_p2
        
        ; Increment Part 2 counter
        inc part2_lo
        bne @skip_p2
        inc part2_hi
        
@skip_p2:
        ; Show progress every 10000 iterations
        lda current_lo
        and #$0F
        bne @no_progress
        lda current_mid
        and #$27
        bne @no_progress
        jsr show_progress
        
@no_progress:
        ; Increment current (24-bit)
        inc current_lo
        bne main_loop
        inc current_mid
        bne main_loop
        inc current_hi
        jmp main_loop

@done:
        ; Print results
        jsr print_results
        
        ; Wait for key
        jsr wait_key
        rts

;=============================================================================
; extract_digits: Convert 24-bit number to 6 decimal digits
; Input: current_lo, current_mid, current_hi
; Output: digits buffer ($10-$15)
;=============================================================================
extract_digits:
        ; Copy current to temp for division
        lda current_lo
        sta temp1
        lda current_mid
        sta temp2
        lda current_hi
        sta temp3
        
        ; Extract each digit by dividing by 10
        ldx #5                  ; Start from rightmost digit
        
@digit_loop:
        ; Divide temp by 10, store remainder as digit
        jsr div10_24bit
        sta digits,x            ; Store remainder (digit)
        
        dex
        bpl @digit_loop
        
        rts

;=============================================================================
; div10_24bit: Divide 24-bit number by 10
; Input: temp1, temp2, temp3 (24-bit dividend)
; Output: temp1, temp2, temp3 (quotient), A (remainder)
; Modifies: temp1, temp2, temp3, A
;=============================================================================
div10_24bit:
        lda #0
        sta temp1+3             ; Remainder = 0
        ldx #24                 ; 24 bits to process
        
@div_loop:
        ; Shift left (temp3:temp2:temp1:remainder)
        asl temp1
        rol temp2
        rol temp3
        rol temp1+3
        
        ; Subtract 10 from remainder if possible
        lda temp1+3
        cmp #10
        bcc @no_sub
        sbc #10                 ; Carry already set
        sta temp1+3
        inc temp1               ; Set bit in quotient
        
@no_sub:
        dex
        bne @div_loop
        
        lda temp1+3             ; Return remainder
        rts

;=============================================================================
; check_part1: Check if password is valid for Part 1
; Input: digits buffer
; Output: A = 1 if valid, 0 if not
; Rules: has adjacent digits AND never decreases
;=============================================================================
check_part1:
        ; Check never decreases
        ldx #0
@check_decrease:
        lda digits,x
        inx
        cpx #6
        beq @check_adjacent
        cmp digits,x
        bcc @invalid            ; digits[i] < digits[i+1] means decrease
        beq @check_decrease     ; Equal is ok
        bcs @check_decrease     ; Greater is ok (never decreases)
        
@check_adjacent:
        ; Check for adjacent matching digits
        ldx #0
@check_adj_loop:
        lda digits,x
        inx
        cpx #6
        beq @invalid
        cmp digits,x
        beq @valid              ; Found adjacent match
        bne @check_adj_loop
        
@valid:
        lda #1
        rts
        
@invalid:
        lda #0
        rts

;=============================================================================
; check_part2: Check if password is valid for Part 2
; Input: digits buffer
; Output: A = 1 if valid, 0 if not
; Rules: has EXACTLY 2 adjacent digits AND never decreases
;=============================================================================
check_part2:
        ; Check never decreases (same as Part 1)
        ldx #0
@check_decrease:
        lda digits,x
        inx
        cpx #6
        beq @check_exact_double
        cmp digits,x
        bcc @invalid
        beq @check_decrease
        bcs @check_decrease
        
@check_exact_double:
        ; Check for exactly 2 adjacent matching digits
        ldx #0                  ; Current position
        
@run_loop:
        cpx #6
        beq @invalid            ; Reached end without finding pair
        
        ; Count consecutive matching digits
        lda digits,x            ; Current digit
        ldy #1                  ; Count = 1
        stx temp1               ; Save position
        
@count_run:
        inx
        cpx #6
        beq @check_count
        cmp digits,x
        bne @check_count
        iny
        jmp @count_run
        
@check_count:
        cpy #2                  ; Is count exactly 2?
        beq @valid
        
        ; Continue to next run
        cpx #6
        bne @run_loop
        beq @invalid
        
@valid:
        lda #1
        rts
        
@invalid:
        lda #0
        rts

;=============================================================================
; Utility routines
;=============================================================================

clear_screen:
        lda #$93                ; Clear screen code
        jsr CHROUT
        rts

show_progress:
        lda #'.'
        jsr CHROUT
        rts

wait_key:
        lda #13
        jsr CHROUT
        ldx #0
@wait_loop:
        lda wait_text,x
        beq @wait_done
        jsr CHROUT
        inx
        bne @wait_loop
@wait_done:
        jsr $FFE4               ; GETIN
        beq @wait_done
        rts

print_results:
        ; Print Part 1 result
        ldx #0
@p1_text:
        lda part1_text,x
        beq @p1_number
        jsr CHROUT
        inx
        bne @p1_text
        
@p1_number:
        lda part1_hi
        ldx part1_lo
        jsr print_16bit
        
        lda #13                 ; Newline
        jsr CHROUT
        
        ; Print Part 2 result
        ldx #0
@p2_text:
        lda part2_text,x
        beq @p2_number
        jsr CHROUT
        inx
        bne @p2_text
        
@p2_number:
        lda part2_hi
        ldx part2_lo
        jsr print_16bit
        
        lda #13
        jsr CHROUT
        rts

;=============================================================================
; print_16bit: Print 16-bit number
; Input: A (hi byte), X (lo byte)
;=============================================================================
print_16bit:
        sta temp2               ; Store hi byte
        stx temp1               ; Store lo byte
        
        ; Convert to decimal string
        ldy #0                  ; Digit count
        
@convert_loop:
        ; Divide by 10
        lda temp1
        ldx temp2
        jsr div16_by_10
        
        ; Push remainder onto stack
        pha
        iny
        
        ; Check if quotient is 0
        lda temp1
        ora temp2
        bne @convert_loop
        
        ; Pop and print digits
@print_loop:
        pla
        ora #$30                ; Convert to ASCII
        jsr CHROUT
        dey
        bne @print_loop
        
        rts

;=============================================================================
; div16_by_10: Divide 16-bit number by 10
; Input: temp1, temp2 (16-bit)
; Output: temp1, temp2 (quotient), A (remainder)
;=============================================================================
div16_by_10:
        lda #0
        sta temp3               ; Remainder
        ldx #16                 ; 16 bits
        
@div16_loop:
        asl temp1
        rol temp2
        rol temp3
        
        lda temp3
        cmp #10
        bcc @no_sub16
        sbc #10
        sta temp3
        inc temp1
        
@no_sub16:
        dex
        bne @div16_loop
        
        lda temp3
        rts

;=============================================================================
; Data
;=============================================================================

title_text:
        .byte 147               ; Clear screen
        .text "advent of code 2019 day 4"
        .byte 13, 13
        .text "range: 248345-746315"
        .byte 13, 13
        .text "computing..."
        .byte 13, 0

part1_text:
        .byte 13
        .text "part 1: ", 0

part2_text:
        .text "part 2: ", 0

wait_text:
        .byte 13
        .text "press any key", 0
