import os
import subprocess

def build_executable(script, spec_path, dist_path):
    """
    Gera um executável para o script Python especificado usando PyInstaller.

    Args:
    - script (str): Caminho completo para o script Python.
    - spec_path (str): Caminho para o diretório onde o arquivo .spec será colocado.
    - dist_path (str): Caminho para o diretório onde a pasta de distribuição será criada.
    """
    script_path = os.path.abspath(script)
    output_folder = os.path.join(dist_path, 'output_exe')  # Pasta de distribuição personalizada 'output_exe'
    command = ['pyinstaller', '--onefile', '--specpath', spec_path, '--distpath', output_folder, script_path]
    
    try:
        subprocess.check_call(command)
        print(f"Executável gerado para {script} com sucesso!")
    except subprocess.CalledProcessError as e:
        print(f"Erro ao gerar executável para {script}: {e}")

def generate_executables(scripts_folder, spec_folder, dist_folder_name):
    """
    Itera sobre todos os arquivos .py na pasta especificada e gera executáveis para cada um.

    Args:
    - scripts_folder (str): Caminho para a pasta onde os scripts Python estão localizados.
    - spec_folder (str): Caminho para o diretório onde os arquivos .spec serão colocados.
    - dist_folder_name (str): Nome da pasta onde a pasta de distribuição será criada.
    """
    dist_path = os.path.join(os.getcwd(), dist_folder_name)  # Diretório de distribuição baseado no diretório de trabalho atual
    
    # Criar a pasta output_exe fora da pasta de distribuição principal
    output_exe_path = os.path.join(dist_path, 'output_exe')
    os.makedirs(output_exe_path, exist_ok=True)

    for file_name in os.listdir(scripts_folder):
        if file_name.endswith('.py'):
            script_path = os.path.join(scripts_folder, file_name)
            build_executable(script_path, spec_folder, dist_path)
