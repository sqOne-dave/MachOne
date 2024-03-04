unit controller_unit;

interface

procedure time_jumper;
procedure check_eingabe(user_input:CHAR);
procedure change_gamespeed(speed:char);

implementation

uses printer_unit,zeiten_unit,globalvar_unit,CRT;

procedure time_jumper;
begin
        print_gamespeed; 
        hour_changer;
        time_printer;
end;

procedure check_eingabe(user_input:CHAR);
begin
        case user_input of 
        '+':    change_gamespeed(user_input);
        '-':    change_gamespeed(user_input);
        end; 
end; 

procedure change_gamespeed(speed:char);
begin
        if (speed = '+') then 
        begin
                case t_game.gamespeed of 
                1:      t_game.gamespeed:= 2;
                2:      t_game.gamespeed:= 4; 
                4:      t_game.gamespeed:= 8;
                8:     t_game.gamespeed:=10;
                end; 
        end
        else if (speed = '-') then
        begin
                case t_game.gamespeed of 
                10:      t_game.gamespeed:= 8;
                8:      t_game.gamespeed:= 4;
                4:      t_game.gamespeed:= 2; 
                2:      t_game.gamespeed:= 1;
                end;
        end;
print_gamespeed; 
GOTOXY(1,2);
write(t_game.gamespeed:2);
end;

end.
