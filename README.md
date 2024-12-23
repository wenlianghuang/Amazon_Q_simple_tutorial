## Amazon Q simple tutorial
- /dev 一個code ```/the/code/you/want/to/generate.py``` =>可以直接產生一個python file
- /test 產生完畢會看**View diff**,確認code沒問題的話就按測試,如果顯示**尚未在此工作區中找到任何測試**,可以按**Configure Python Tests** => 選**pytest** => 選 **test** =>按測試即可
- /doc => 直接產生README.md, ctrl+s 儲存他
- /review 這邊有個我的[github](https://github.com/wenlianghuang/Stock_Web_Record.git)可以clone下來直接review

#### Pro
- 描述完整
- review可以考慮安全性的建議
- 可以直接產生**README.md**
#### Con
- 速度慢
- test只支援python & java
- 無法對每個code進行詳細的command(有待討論)