echo Run Tesseract for Training.. 
tesseract alpha.font.exp0.tif alpha.font.exp0 nobatch alpha.train 

echo Compute the Character Set.. 
#unicharset_extractor alpha.font.exp0.box 
mftraining -F font_properties -U unicharset -O alpha.unicharset alpha.font.exp0.tr 


echo Clustering.. 
cntraining alpha.font.exp0.tr 

echo Rename Files.. 
rename normproto alpha.normproto 
rename inttemp alpha.inttemp 
rename pffmtable alpha.pffmtable 
rename shapetable alpha.shapetable  

echo Create Tessdata.. 
combine_tessdata alpha.

echo. & pause