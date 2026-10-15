#!/bin/zsh
cd /Users/nishal/PROJECTS/jobbot/ai-job-search
for n in 1 2 3 4 5 6 7 8 9 10; do
  codex exec -s workspace-write --skip-git-repo-check -C "$(pwd)" - < scratchpad/rank_batch_$n.txt > scratchpad/rank_out_$n.json 2>scratchpad/rank_err_$n.log
  echo "batch $n exit $?" >> scratchpad/progress.log
done
echo done >> scratchpad/progress.log
