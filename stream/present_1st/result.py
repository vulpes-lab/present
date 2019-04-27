from stream.present import Present

supporters = '@c:kyoka_0128', '@nac335', '@ c:CapMuffin', '@limeh12', '@miyachanss', '@oxk_i6halcyon', '@tarte_tatin_227', \
             '@si_ta_t', '@ZhW3BH6iC9LKLLr', '@tanaka5656hoo', '@GReen_APP5', '@rufu101010', '@Lta4Oep4Qg5JAdz', '@Ru_u_tya', \
             '@rrr_f20', '@iku30523'

seed = '吉田くん'
present = Present(supporters, seed)

print('suppoters:', supporters)
print('seed:', seed)

print('当選者1: ', present.lottery())
print('当選者2: ', present.lottery())
print('当選者3: ', present.lottery())
