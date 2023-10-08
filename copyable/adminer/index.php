<?php

function adminer_object()
{
    require_once __DIR__ . '/plugins/plugin.php';
    require_once __DIR__ . '/AdminerDefaultServer.php';

    // Include all plugin files, if any
    foreach (glob(__DIR__ . '/plugins/*.php') as $filePath) {
        require_once $filePath;
    }

    return new AdminerDefaultServer([
        // new PluginClass(),
    ]);
}

// Include original Adminer or Adminer Editor
require_once __DIR__ . '/adminer.php';
