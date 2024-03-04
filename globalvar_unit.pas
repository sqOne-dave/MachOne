unit globalvar_unit;

interface

type
        time_stemp = record
                hour: byte;
                day:byte;
                wday:byte;
                month:byte;
                X_year:boolean;
                year:INTEGER;
end;

type 
        user_settings = record
                gamespeed: byte;
end;

var t:time_stemp;
t_game:user_settings;
//0=holz,1=stein,2=essen,3=eisen,4=gold
ress_ar: array[0..23,0..4] of INTEGER; 

implementation

initialization

t.hour := 0;
t.day := 1;
t.wday := 1;
t.month := 1;
t.X_year := true;
t.year := 0;

t_game.gamespeed := 1;

end.
