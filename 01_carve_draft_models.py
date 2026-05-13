import os
import subprocess

working_dir = '/home/emma/Dokumente/thesis/Model_generation_curation'
annotated_genomes_dir = os.path.join(working_dir, 'genome_files')
gram_neg_dir = os.path.join(annotated_genomes_dir, 'gram_negative')
gram_pos_dir = os.path.join(annotated_genomes_dir, 'gram_positive')
gram_unknown_dir = os.path.join(annotated_genomes_dir, 'gram_unknown')
draft_model_dir = os.path.join(working_dir, 'Draft_models')

def carve_models(sequence_dir, universe):
    for file in os.listdir(sequence_dir):
        if file.endswith('.fa'):
            sequence_path = os.path.join(sequence_dir, file)
            draft_path = os.path.join(draft_model_dir, f'{file[:-3]}.xml')
                
            if os.path.exists(draft_path):
                print(f'Skipping {file}: Model already exists at {draft_path}')
                continue
            print(f'Starting carving process for {file}')
            subprocess.run([
                        'conda', 'run', '-n', 'GEMS_creation',
                        'carve', '--dna', sequence_path, 
                        '--output', draft_path,
                        '-u', universe 
                    ], check=True)
            print(f'Finished carving process for {file}')
    
carve_models(gram_neg_dir, 'gramneg')
carve_models(gram_pos_dir, 'grampos')
carve_models(gram_unknown_dir, 'bacteria')
