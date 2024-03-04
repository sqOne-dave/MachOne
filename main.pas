program main;
uses CRT,zeiten_unit,controller_unit,globalvar_unit;

procedure start;
var eingabe:char;

begin
cursoroff;
clrscr;
        while not( eingabe = 'q') do
        begin
                        repeat
                                taktung(t_game.gamespeed);
                        until KeyPressed;
        eingabe:=readkey;
        if (eingabe <> 'q')then check_eingabe(eingabe);
        end;
cursoron;
end;

begin
clrscr;
(*Das ist Code der nicht ausgef�hrt wird*)
start;
(*readkey;*)
end.
