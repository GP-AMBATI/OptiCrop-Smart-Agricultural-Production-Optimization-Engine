from model import ensure_artifacts, train_and_save


if __name__ == '__main__':
    print('Training OptiCrop model...')
    best_model, results = train_and_save()
    print(f'Best model selected: {best_model}')
    print('Training complete. Artifacts saved in project root.')
