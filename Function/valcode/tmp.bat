echo Run Tesseract for Training..
D:\Python3.8.6\Tesseract_OCR\tesseract.exe num.font.exp0.tif num.font.exp0 nobatch box.train
echo Compute the Character Set..
D:\Python3.8.6\Tesseract_OCR\unicharset_extractor.exe num.font.exp0.box
D:\Python3.8.6\Tesseract_OCR\mftraining -F font_properties -U unicharset -O num.unicharset num.font.exp0.tr
echo Clustering..
D:\Python3.8.6\Tesseract_OCR\cntraining.exe num.font.exp0.tr
echo Rename Files..
rename normproto num.normproto
rename inttemp num.inttemp
rename pffmtable num.pffmtable
rename shapetable num.shapetable
echo Create Tessdata..
D:\Python3.8.6\Tesseract_OCR\combine_tessdata.exe num.