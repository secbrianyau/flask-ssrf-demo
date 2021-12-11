#!/bin/bash
kill $(ps aux | grep flask | grep -v 'grep' | awk '{print $2}')
