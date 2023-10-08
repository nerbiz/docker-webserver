<?php

class AdminerDefaultServer extends AdminerPlugin
{
    function credentials(): array
    {
        // Get the original credentials
        $credentials = parent::credentials();

        // Set the server name from a file, if it exists
        $serverNameFile = __DIR__ . '/servername.txt';
        $credentials[0] = (is_readable($serverNameFile))
            ? trim(file_get_contents($serverNameFile))
            : 'localhost';

        return $credentials;
    }
}
