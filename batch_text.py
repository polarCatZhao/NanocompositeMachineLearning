import os, glob, PyPDF2, re

pattern = 'D:\data\*'
folders = glob.glob(pattern)

found_matches = dict()
found_matches['heating_rate'] = 0
found_matches['dma_mode'] = 0
found_matches['filler_aratio'] = 0
found_matches['spherical'] = 0
found_matches['colloidal'] = 0
found_matches['powder'] = 0
found_matches['diameter'] = 0
found_matches['cluster_d'] = 0
found_matches['ssa']=0
found_matches['in_situ']=0
found_matches['melt_mixing']=0
found_matches['solution_processing']=0
found_matches['sol_gel']=0
found_matches['tip_sonication']=0
found_matches['bath_sonication']=0
found_matches['surfactant']=0
found_matches['acetone']=0
found_matches['catalyst']=0
for folder in folders:
    print(folder)
    paper_txt = glob.glob(folder + '\paper.txt')[0]
    with open(paper_txt,'r', encoding='utf-8') as f:
        text = f.read()

        heating_rate_matches = re.findall('\d+[ \n]*°C/min', text)
        heating_rate_matches += re.findall('\d+[ \n]*8C/min', text)
        heating_rate_matches += re.findall('\d+[ \n]*oC/min', text)
        heating_rate_matches += re.findall('scanning[ \n]*rate[ \n]*of[ \n]*\d+[ \n]*', text)
        heating_rate_matches += re.findall('heating[ \n]*rate[ \n]*of[ \n]*\d+[ \n]*', text)
        print(heating_rate_matches)
        if heating_rate_matches:
            found_matches['heating_rate'] +=1


        dma_mode_matches = re.findall('[Dd]ynamic[ \n]*mechanical[ \n]*test',text)
        dma_mode_matches += re.findall('DMA', text)
        dma_mode_matches += re.findall('[Dd]ynamic[ \n]*mechanical[ \n]*analysis',text)
        print(dma_mode_matches)
        if dma_mode_matches:
            found_matches['dma_mode'] += 1


        filler_aratio_matches = re.findall('aspect ratio', text)
        print(filler_aratio_matches)
        
        if filler_aratio_matches:
            found_matches['filler_aratio'] += 1



        spherical_matches = re.findall('spherical', text)
        print(spherical_matches)

        if spherical_matches:
            found_matches['spherical'] += 1


        colloidal_matches = re.findall('colloidal', text)
        colloidal_matches += re.findall('sol[- \n]phase', text)
        print(colloidal_matches)

        if colloidal_matches:
            found_matches['colloidal']+=1


        powder_matches = re.findall('powder', text)
        print(powder_matches)

        if powder_matches:
            found_matches['powder'] += 1


        diameter_matches = re.findall('diameter', text)
        print(diameter_matches)

        if diameter_matches:
            found_matches['diameter'] += 1


        cluster_d_matches = re.findall('cluster diameter', text)
        print(cluster_d_matches)

        if cluster_d_matches:
            found_matches['cluster_d'] += 1


        ssa_matches = re.findall('specific[ \n]*surface[ \n]*area', text)
        print(ssa_matches)

        if ssa_matches:
            found_matches['ssa'] += 1


        in_situ_matches = re.findall('in[- \n]*situ[ \n]', text)
        print(in_situ_matches)

        if in_situ_matches:
            found_matches['in_situ']+=1


        melt_mixing_matches = re.findall('melt[- \n]*mixing', text)
        print(melt_mixing_matches)

        if melt_mixing_matches:
            found_matches['melt_mixing'] += 1


        solution_processing_matches = re.findall('solution[- \n]processing',text)
        print(solution_processing_matches)

        if solution_processing_matches:
            found_matches['solution_processing'] += 1


        sol_gel_matches = re.findall('sol[- \n]gel[ \n]', text)
        print(sol_gel_matches)

        if sol_gel_matches:
            found_matches['sol_gel'] +=1


        tip_sonication_matches = re.findall('tip[- \n]sonication', text)
        print(tip_sonication_matches)

        if tip_sonication_matches:
            found_matches['tip_sonication'] += 1

        bath_sonication_matches = re.findall('bath[- \n]sonication', text)
        print(bath_sonication_matches)

        if bath_sonication_matches:
            found_matches['bath_sonication'] += 1


        surfactant_matches = re.findall('surfactant', text)
        print(surfactant_matches)

        if surfactant_matches:
            found_matches['surfactant'] += 1


        acetone_matches = re.findall('acetone', text)
        print(acetone_matches)

        if acetone_matches:
            found_matches['acetone'] += 1

        catalyst_matches = re.findall('catalyst', text)
        print(catalyst_matches)
        if catalyst_matches:
            found_matches['catalyst'] += 1


print('found matches : ')
print(found_matches)

#print(list(enumerate(folders)))
"""
paper_txt = glob.glob(folders[63]+'\paper.txt')[0]
with open(paper_txt, 'r', encoding='utf-8') as f:
    text = f.read()
    matches = re.findall('heating[ \n]*rate[ \n]*of[ \n]*\d+[ \n]*°*C/min', text)
    print(matches)
"""