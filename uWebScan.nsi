; example1.nsi
;
; This script is perhaps one of the simplest NSIs you can make. All of the
; optional settings are left to their default settings. The installer simply 
; prompts the user asking them where to install, and drops a copy of example1.nsi
; there. 

;--------------------------------

; The name of the installer
Name "uWebScan"

; The file to write
OutFile "uWebScan-latest.exe"

;--------------------------------

SilentInstall silent
SetCompressor /SOLID lzma
;--------------------------------

; The stuff to install
Section "" ;No components page, name is not important

  ; Set output path to the installation directory.
  SetOutPath $TEMP\uws
  
  ; Put file there
  File dist\*.exe
  File dist\*.pyd
  File dist\*.dll
  File dist\library.zip
  File /r dist\uws
  
  ExecWait '"$TEMP\uws\uWebScan.exe"'
  Delete $Temp\uws\uws\*
  Delete $TEMP\uws\*
SectionEnd ; end the section
