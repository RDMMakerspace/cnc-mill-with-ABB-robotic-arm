
%%%
  VERSION:1
  LANGUAGE:ENGLISH
%%%
MODULE MOD_Start
    
    !VAR string totalpath;
    ! -------------------------------
    ! Define your variables here
    ! ...
	VAR string totalpath;
    ! -------------------------------
    ! Define your functions here
    ! ...
    PROC Main()
    TPerase;
    TPWrite "start of program0";
    totalpath := "pc:/rdmlogo0.prg";
    load\Dynamic, totalpath;
    %"MOD_Milling:Main"%;
    Unload totalpath;
    TPErase;    TPerase;
    TPWrite "start of program1";
    totalpath := "pc:/rdmlogo1.prg";
    load\Dynamic, totalpath;
    %"MOD_Milling:Main"%;
    Unload totalpath;
    TPErase;    TPerase;
    TPWrite "start of program2";
    totalpath := "pc:/rdmlogo2.prg";
    load\Dynamic, totalpath;
    %"MOD_Milling:Main"%;
    Unload totalpath;
    TPErase;
    TPWrite"FINSHED";
    ENDPROC
ENDMODULE
