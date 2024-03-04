unit zeiten_unit;

interface

procedure taktung(gamespeed:INTEGER);
procedure hour_changer;
procedure day_changer;
procedure weekday_changer;
procedure month_changer;
procedure year_changer;
function check_x_year:boolean;

implementation
//1 Tag = 4 Sekunden vier verschieden Tageszeiten
uses CRT,controller_unit,globalvar_unit;

procedure taktung(gamespeed:INTEGER);
begin
        case gamespeed of
                1: delay(1000);
                2: delay(500);
                4: delay(250);
                8: delay(125);
                10: delay(0);
        end;
time_jumper;
end;

procedure hour_changer;
begin
        case t.hour of
                0..22:  t.hour:= t.hour + 1;
                23:     begin
                                t.hour:= 0;
                                day_changer;
                        end;
        end;
end;

procedure day_changer;
var feb_days :INTEGER = 30; 
begin
t.day := t.day + 1;
weekday_changer;
        case t.month of
                1,3,5,7,10,12:        begin
                                                if (t.day >= 32 ) then
                                                begin
                                                        t.day := 1;
                                                        month_changer;
                                                end;
                                        end;

                2:                      begin
                                                if t.X_year = true then feb_days := 30 else feb_days := 29; 
                                                if (t.day >= feb_days ) then
                                                begin
                                                        t.day := 1;
                                                        month_changer;
                                                end;
                                        end;
                4,6,8,9,11:             begin
                                                if (t.day >= 31 ) then
                                                begin
                                                        t.day := 1;
                                                        month_changer;
                                                end;
                                        end;
        end;

end;

procedure weekday_changer;
begin
t.wday:= t.wday + 1;
if (t.wday = 8) then  t.wday:= 1;
end;

procedure month_changer;
begin
t.month:= t.month + 1;
if (t.month >= 13) then 
        begin
                t.month:= 1;
                year_changer;
        end;
end;

procedure year_changer;
begin
        t.year := t.year + 1;
        t.X_year:= check_x_year; 
end;

function check_x_year:boolean;
var erg : INTEGER = 0;  
begin
        erg:= t.year MOD 4;
        if (erg = 0) then check_x_year:= true else check_x_year:= false;
end; 

end.
