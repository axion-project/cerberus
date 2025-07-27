#!/usr/bin/env python3
"""
Cerberus AI Security - Main Entry Point
"""
import logging
import argparse
from cerberus.watchman import WatchmanHead
from cerberus.config import load_config

def main():
    parser = argparse.ArgumentParser(description='Cerberus AI Security')
    parser.add_argument('--config', default='config/default.yaml')
    args = parser.parse_args()
    
    config = load_config(args.config)
    logging.basicConfig(level=config.log_level)
    
    # Initialize watchman head
    watchman = WatchmanHead(config.watchman)
    watchman.start_monitoring()

if __name__ == "__main__":
    main()
