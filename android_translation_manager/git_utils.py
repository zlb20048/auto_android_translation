import subprocess
import logging
from pathlib import Path
import os

def get_git_root(path):
    try:
        git_root = subprocess.check_output(['git', '-C', str(path), 'rev-parse', '--show-toplevel'], stderr=subprocess.DEVNULL)
        logging.info(f"git_root ---> {git_root}")
        return Path(git_root.decode('utf-8').strip())
    except subprocess.CalledProcessError:
        parent = path.parent
        if parent == path:
            logging.warning(f"无法获取 git 根目录: {path}")
            return None
        return get_git_root(parent)

def clone_repo(base_dir, repo_url, branch):
    logging.info("开始克隆代码仓库")
    try:
        base_dir.mkdir(parents=True, exist_ok=True)
        os.chdir(base_dir)
        env = os.environ.copy()
        env['LANG'] = 'en_US.UTF-8'
        env['LC_ALL'] = 'en_US.UTF-8'

        # 执行 repo init
        subprocess.run(["repo", "init", "-u", repo_url, "-b", branch], env=env, check=True)

        # 执行 repo sync
        subprocess.run(["repo", "sync"], env=env, check=True)

        logging.info("代码仓库克隆完成")
    except subprocess.CalledProcessError as e:
        logging.error(f"克隆仓库失败: {e}")
        raise
    except Exception as e:
        logging.error(f"克隆仓库时发生未知错误: {e}")
        raise
