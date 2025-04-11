total_seconds = int(12345)
hour = total_seconds // 3600
reamin_seconds = total_seconds % 3600
minutes = reamin_seconds // 60
seconds = reamin_seconds % 60

print('12345초는', hour, '시간', minutes, '분', seconds, '초입니다.')
 