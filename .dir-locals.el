((nil
  (eval . (let* ((root (projectile-project-root)))
	    (setq-local lsp-jedi-workspace-extra-paths
			(vector (concat root "env/lib/python3.11/site-packages")))))))
