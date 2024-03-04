program main;
uses CRT,zeiten_unit,controller;

procedure start;
var eingabe:char;
begin
        while not( eingabe = 'q') do
        begin
                        repeat
                                taktung(1); 
                        until KeyPressed;
        eingabe:=readkey;
        end;
end;

begin
clrscr;
(*Das ist Code der nicht ausgef�hrt wird*)
start;
(*readkey;*)
end.