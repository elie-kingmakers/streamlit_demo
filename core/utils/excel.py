from pathlib import Path
import shutil
from typing import Dict, Union

import pandas as pd


def write_excel_file(sheetsToWrite: Dict[str, pd.DataFrame], outputFile: Union[str, Path]) -> None:
    outputFile = Path(outputFile)
    tempFilename = f"./{outputFile.stem}"  # can't write to dbfs directly, need local node and then transfer
    excelWriter = pd.ExcelWriter(tempFilename, engine="xlsxwriter")  # pylint: disable=abstract-class-instantiated
    for key, dataframe in sheetsToWrite.items():
        dataframe.to_excel(excel_writer=excelWriter, sheet_name=key[:30], index=False)
    excelWriter.save()
    Path(outputFile.parent).mkdir(parents=True, exist_ok=True)
    shutil.move(tempFilename, outputFile)
