unit printer_unit;

interface

procedure time_printer;
function print_wday(wday:INTEGER):String;
function print_month(month:INTEGER):String;
procedure print_gamespeed;

implementation
USES CRT,globalvar_unit;

procedure time_printer;
begin
        GOTOXY(1,1); 
        write(t.hour:2);
        GOTOXY(4,1);
        write(print_wday(t.wday):3);
        GOTOXY(8,1);
        write(t.day:2);
        GOTOXY(11,1);
        write(print_month(t.month):3);
        GOTOXY(15,1);
        write(t.year:4);   
end;

function print_wday(wday:INTEGER):String; 
var days_array: array[1..7] of String = ('Mon','Die','Mit','Don','Fri','Sam','Son');
begin
    print_wday:= days_array[wday];
end;

function print_month(month:INTEGER):String;
var month_array: array[1..12] of String = ('Jan','Feb','Mar','Apr','Mai','Jun','Jul','Aug','Sep','Okt','Nov','Dez');
begin
    print_month:= month_array[month];
end;

procedure print_gamespeed;
var print_text:String = '1'; 
begin
    case t_game.gamespeed of 
    1:  print_text:='1'; 
    2:  print_text:='2'; 
    4:  print_text:='3';
    8:  print_text:='4';
    10: print_text:='5';
    end; 
GOTOXY(20,1);
write('Game-Speed: ',print_text,'x');  
end;

end.